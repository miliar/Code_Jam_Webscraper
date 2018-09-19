import sys

def main():    
    tcs = int(sys.stdin.readline())
    for t in range(1, tcs+1):
        a,b,k=map(lambda x: int(x), sys.stdin.readline().strip().split())
        #print a,b,k
        counter = 0
        for i in range(a):
            for j in range(b):
                if i&j < k:
                    #print i,j
                    counter+=1
        print "Case #" + str(t) + ": " + str(counter)
        





if  __name__ =='__main__':main()
