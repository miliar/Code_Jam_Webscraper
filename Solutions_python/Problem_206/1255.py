def cruiseSpeed(distance,n,horses):
    max_time=0
    for horse in horses:
        time=(distance-horse[0])/float(horse[1])
        if time>max_time:
            max_time=time
    return float(distance)/max_time
    
def main(fin,fout):
    numCases=int(fin.readline())
    for i in range(numCases):
        case=fin.readline().split()
        distance=int(case[0])
        n=int(case[1])
        horses=[]
        for j in range(n):
            horse=fin.readline().split()
            horses.append((int(horse[0]),int(horse[1])))
        fout.write('Case #'+str(i+1)+': '+str(cruiseSpeed(distance,n,horses))+'\n')
        
fin=open('C:\\Users\\exin1\\Google Drive\\Study\\programming\\Google CodeJam 2017\\1B\\1.in','r')
fout=open('C:\\Users\\exin1\\Google Drive\\Study\\programming\\Google CodeJam 2017\\1B\\1.out','w')
main(fin,fout)
fin.close()
fout.close()