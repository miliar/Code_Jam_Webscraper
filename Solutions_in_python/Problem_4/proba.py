import os
import sys
import time
sys.setrecursionlimit(10000)

class timeObj:
	def __init__(self,second):
		self.value=second

class station:
	def __init__(self,timeList=[],turnOverTime=0,name=''):
		self.name=name
		self.needed=0
		self.members=0
		self.turnOverTime=turnOverTime*60
		self.timeList=[]
		self.arriveList=[]
		self.addTime(timeList)

	def getNeeded(self):
		return self.needed

	def inTransit(self,arriveList):
		self.arriveList+=arriveList

	def addTime(self,timeList):
		for depart,arrive in timeList:
			depart=self.convertTime(depart)
			arrive=self.convertTime(arrive)
			self.timeList.append([depart,arrive])
		return 1

	def convertTime(self,value):
		HH,MM=value.split(":")
		seconds=3600*int(HH) + 60*int(MM)
		#print "%s == %s" % (value,seconds)
		return timeObj(seconds)

	def depart(self):
		if self.members:
			self.members-=1
			self.log("member %s" % self.members)
		else:
			self.needed+=1
			self.log("needed %s" % self.needed)
	def arrive(self):
		self.members+=1

	def log(self,text):
		pass
		#print "%s %s" % (self.name,text)

	def checkTime(self,timer):
		otherTimes=[]
		for arrive in list(self.arriveList):
			if (arrive.value+self.turnOverTime) ==timer:
				self.log("ARRIVE %s" % timer)
				self.arrive()
				self.arriveList.remove(arrive)
		for depart,arrive in list(self.timeList):
			if depart.value == timer:
				self.log("DEPART %s" % timer)
				self.depart()
				otherTimes.append(arrive)
				#print self.timeList
				self.timeList.remove([depart,arrive])

		#for arrive in list(self.arriveList):
		#	if (arrive.value+self.turnOverTime) ==timer:
		#		self.log("ARRIVE %s" % timer)
		#		self.arrive()
		#		self.arriveList.remove(arrive)
		return otherTimes
				



class parser:
	def __init__(self):
		self.MAXTIME=3600*24
		pass

	def run(self,set1,set2):
		i=0
		xHigh=[]
		xLow=[]
		xZero=[]
		yHigh=[]
		yLow=[]
		yZero=[]
		MAX=len(set1)
		while i <  MAX:
			
			x=int(set1[i])
			if x < 0:
				xLow.append(x)
			elif x == 0:
				xZero.append(x)
			else:
				xHigh.append(x)
			y=int(set2[i])
			if y < 0:
				yLow.append(y)
			elif x == 0:
				yZero.append(y)
			else:
				yHigh.append(y)
			
			i+=1

		X=xHigh+xLow+xZero
		Y=yHigh+yLow+yZero

		X.sort()
		Y.sort()
		Y.reverse()
		return self.calc(X,Y,MAX)

	def calc(self,X,Y,MAX):
		i=0
		num=0
		#print X
		#print Y
		while i < MAX:
			num+=(X[i]*Y[i])
			i+=1
		return num
			

	def parse(self,filename):
		result=[]
		data=file(filename,'r').readlines()
		print len(data)
		T=int(data[0].strip())
		n=1
		i=1
		result=[]
		#T=int(data[i])
		#i+=1

		while n <= T:
			#T=int(data[i])
			#i+=1
			N=data[i]
			#NA,NB=data[i].split()
			i+=1
			set1=data[i].split()
			i+=1
			set2=data[i].split()
			i+=1
			a=''
			#print set1,set2
			print n
			a=self.run(set1,set2)
			#print "n: %s" % n
			#a,b=self.run(naList,nbList,T)
			result.append("Case #%s: %s" % (n,a))
			print "DONE"
			n+=1
			#print "N: %s" % N
			#print "T: %s" % T
			#print "NA: %s" % NA
			##print "NALIST: %s" % naList
			#print "NB: %s" % NB
			#print "NBLIST: %s" % nbList
		return result


if __name__ == "__main__":
	filename=sys.argv[1]
	outfilename=sys.argv[2]
	start=time.time()
	print time.ctime()
	a=parser()
	result=a.parse(filename)
	print "RESULT"
	print "\n".join(result)
	print "Written to %s" % outfilename
	file(outfilename,'w').write("\n".join(result))
	end=time.time()
	print (end - start)
	print time.ctime()
	#for key,item in a.queryData.items():
	#	print "final %s %s" % (key,a.recurse(a.queryData[key]))
#	print a.queryData
#	print len(a.queryData[1])
#	print a.searchEngines

