import string
#import pdb
class Train_Timetable:
    def __init__(self,tr,a_trip,b_trip):
        self.tr=tr
        self.a_trip=a_trip
        self.b_trip=b_trip
        self.a=0
        self.b=0
        self.trains=[]

    def run(self):
        self.a_trip.sort()
        self.b_trip.sort()
        #print self.a_trip
        #print self.b_trip
        while len(self.a_trip)>0 or len(self.b_trip)>0:
            if len(self.b_trip)==0 :
                sta=1
                trip=self.a_trip[0]
                self.a_trip=self.a_trip[1:]
            elif len(self.a_trip)==0 or self.a_trip[0][0]>self.b_trip[0][0]:
                sta=2
                trip=self.b_trip[0]
                self.b_trip=self.b_trip[1:]
            else:
                sta=1
                trip=self.a_trip[0]
                self.a_trip=self.a_trip[1:]
                
            tid=self.check_trains(trip[0],sta)
            print sta,tid,trip
            if tid ==-1:
                newtrain=[sta,sta,trip]
                self.trains.append(newtrain)
            else:
                self.trains[tid][1]=sta
                self.trains[tid][2]=trip
                
        ta=0
        tb=0
        for train in self.trains:
            if train[0]==1:
                ta+=1
            if train[0]==2:
                tb+=1
        self.a = ta 
        self.b = tb 
            
        return
    def check_trains(self,timepoint,sta):
        tid=-1
        index =0
        #pdb.set_trace()
        for train in self.trains:
            if train[2][1]+self.tr <= timepoint:
                if train[1]==1 or train[1]==4:
                    train[1]=4
                    if sta==2:
                        tid=index
                if train[1]==2 or train[1]==3:
                    train[1]=3
                    if sta==1:
                        tid=index
            index +=1
                    
        return tid

pid=1
ff=open("B-large.in")
ww=open("B-large.out","w")
ll=ff.readline()
num=string.atoi(ll)
while pid<=num:
    #print "++++++++++++++%d++++++++++++++++++++++"%(pid)
    ll=ff.readline()
    tr_time=string.atoi(ll)
    ll=ff.readline()
    temp=ll.split()
    a_sum=string.atoi(temp[0])
    b_sum=string.atoi(temp[1])
    a_trip=[]
    b_trip=[]
    for i in range(a_sum):
        ll=ff.readline()
        temp=ll.split()
        table=[]
        for t in temp:
            temp2=t.split(':')
            table.append(string.atoi(temp2[0])*60+string.atoi(temp2[1]))
        a_trip.append(table)
    for i in range(b_sum):
        ll=ff.readline()
        temp=ll.split()
        table=[]
        for t in temp:
            temp2=t.split(':')
            table.append(string.atoi(temp2[0])*60+string.atoi(temp2[1]))
        b_trip.append(table) 

    tt=Train_Timetable(tr_time,a_trip,b_trip)
    tt.run()
    ww.write("Case #%d: %d %d\n"%(pid,tt.a,tt.b))
    print "Case #%d: %d %d\n"%(pid,tt.a,tt.b)
    pid +=1
    
ff.close()
ww.close()
