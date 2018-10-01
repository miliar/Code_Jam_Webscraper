fin="/home/aksh/B-small-attempt0.in"
fout="B.txt"
file = open(fin, "r")
t=int(file.readline())

arr=[]
ans=[]
for i in range(t):
    temparr = map(int,file.readline().strip().split(' '))
    print temparr
    arr.append(temparr)
    
##t=100
##for i in range(t):
##    arr.append([100,i+1])
##   
##
    
for i in range(t):

    if arr[i][1] > arr[i][0]/2 or arr[i][3] > arr[i][0]/2  or  arr[i][5] > arr[i][0]/2:
        strans = "IMPOSSIBLE"
    else:

        if arr[i][1] >= arr[i][3] and arr[i][1] >= arr[i][5]:
            maxchar = 'R'
            maxsize = arr[i][1]
            next1char = 'Y'
            next2char = 'B'
            next1size = arr[i][3]
            next2size = arr[i][5]
        elif arr[i][3] >= arr[i][1] and arr[i][3] >= arr[i][5]:
            maxchar = 'Y'
            maxsize = arr[i][3]
            next1char = 'R'
            next2char = 'B'
            next1size = arr[i][1]
            next2size = arr[i][5]

        else:
            maxchar = 'B'
            maxsize = arr[i][5]
            next1char = 'Y'
            next2char = 'R'
            next1size = arr[i][3]
            next2size = arr[i][1]

        j=0
        k=0
        strans = maxchar*maxsize

        while j < maxsize and k < next1size:
            print strans
            strans = strans[0:2*j+1] + next1char + strans[2*j+1:]
            j = j + 1
            k = k + 1

        k=0
        while j < maxsize and k < next2size:
            print strans

            strans = strans[0:2*j+1] + next2char + strans[2*j+1:]
            j = j + 1
            k = k + 1

        j=0

        while k < next2size:
            print strans
            strans = strans[0:3*j+1] + next2char + strans[3*j+1:]
            j = j + 1
            k = k + 1

   
    print strans


    ans.append(strans)
            
        
print ans

file.close()
file = open(fout, "w")

for i in range(t):
    file.write("Case #"+str(i+1)+": "+ans[i]+'\n')
file.close()

