'''
Created on Feb 22, 2017

@author: cturkarslan
'''
###REDIRECT IO
import sys
sys.stdin = open('A-small-attempt1.in' ,'r')
#sys.stdin = open('Input.in' ,'r')
sys.stdout = open('output.txt' , 'w')


T = int(input())
for t in range(T):
    D,N = map(int,input().split())
    horses = []
    for n in range(N):
        (k,s) = map(int,input().split())
        hours = (D-k)/s 
        for horse in horses:
            if(s > horse[1]):
                catchup_time = (k-horse[0])/(s-horse[1])
                if catchup_time > hours:
                    hours = catchup_time
        horses.append((k,s,hours))
#    print(horses)
    horses = sorted(horses,key=lambda tup: tup[2],reverse = True)
                          
    print ("Case #%d:" %(t+1),D/horses[0][2])

if __name__ == '__main__':
    pass


