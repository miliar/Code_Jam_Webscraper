#!/usr/bin/python


def standing_ovation(case_num):
    snum,values=raw_input().split()
    front=0
    new_added=0
    for si,num in enumerate(values):
        if front < si:
            new_added_req = si-front
            new_added = new_added+new_added_req
            front = si
        front = front+int(num)
    print "Case #%s: %s"%(case_num,new_added)




def main():
    k=int(raw_input())
    for i in xrange(k):
        standing_ovation(i+1)

if __name__ == "__main__":
    main()