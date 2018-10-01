__author__ = 'rainp1ng'

def main(inr,outr):
    t=int(inr.readline())
    for i in range(t):
        outr.write("Case #%s: "%(i+1)+solve(inr)+"\n")

def solve(inr):
    print "+++++++++++++++++++++++++++++++++++++++++++++"
    data=inr.readline().split()
    max_level=int(data[0])
    stat=data[1]
    stat_list=[]
    for val in stat:
       stat_list.append(int(val))

    result=0
    for i in range(1,max_level+1):
        if stat_list[i]>0:
           d=i-sum_p(i,stat_list)
           if d>0:
                result+=d
                stat_list[i-1]+=d
    print "case:",result
    return str(result)

def sum_p(n,stat_list):
    sum=0
    for i in range(n):
        sum+=stat_list[i]
    #print n,":",sum
    return sum

inr=open("/Users/rainp1ng/Downloads/Contest/GoogleCodeJam/identification_round/A-large.in","rb")
outr=open("/Users/rainp1ng/Downloads/Contest/GoogleCodeJam/identification_round/output","wb")

main(inr,outr)
