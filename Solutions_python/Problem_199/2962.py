from os.path import expanduser

problem = "A-large"
path = expanduser('C:/Users/SWAPNIL/Downloads/')
file_in = path + problem + '.in'
file_out = path + problem + '.out'
      
with open(file_in,'rb') as fin, open(file_out,'wb') as fout:
    lines = fin.read().splitlines()
    case = 1
    for l in lines[1:]:
        s,k=l.split(' ')
        k=int(k)
        count=0
        flag=1
        ans=s[:]
        for j in range(0,len(s)-k+1):
            if ans[j]=="-":
                count+=1
                for z in range(j,j+k):
                    if ans[z] =="-":
                        ans=(ans[0:z]+"+"+ans[z+1:])
                    else:
                        ans=(ans[0:z]+"-"+ans[z+1:]) 
        for j in range(0,len(s)):
            if ans[j]=="-":
                flag=0
                break
        if flag==1:
            answer=str(count)
        else:
            answer="IMPOSSIBLE"    
        output = 'Case #%d: %s\n' % (case,answer)
	fout.write(output)
	case += 1