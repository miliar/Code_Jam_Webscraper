import re
import sys
buf=[]
def scans():
 global buf
 while 1:
  while len(buf) <= 0: buf=input().replace('\n',' ').split(' ')
  o=buf.pop(0)
  if o!='': break
 return o
def scan(): return int(scans())

sys.stdin = open('input.txt')
ofg=1
if ofg:
 sys.stdout = open('output.txt','w')


#Code Here
def perm(pref,n,cnt):
    if(cnt<0 or cnt>n):
        return
    if(n>=1):
        pref[n-1]=0
        for i in perm(pref,n-1,cnt):
            yield i
        pref[n-1]=1
        for i in perm(pref,n-1,cnt-1):
            yield i
    else:
        yield(pref)

def calc(w,h,n):
    mz = 9999999
    for i in perm([0]*(w*h),w*h,n):
        cnt = 0
        #vert wall
        for y in range(h):
            for x in range(w-1):
                if(i[x+y*w] and i[x+1+y*w]):
                    cnt+=1
        #horz wall
        for y in range(h-1):
            for x in range(w):
                if(i[x+y*w] and i[x+(y+1)*w]):
                    cnt+=1
        mz = min(mz,cnt)
    return mz

for t in range(scan()):
    w,h,n = scan(),scan(),scan()
    print('Case #%d: %d'%(t+1,calc(w,h,n)))


if ofg:
 sys.stdout.flush()
 sys.stdout.close()
 sys.stderr.write("OK\n")