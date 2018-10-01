'''
Created on May 7, 2010

@author: user1
'''
t = [2, 4, 2, 3, 4, 2, 1, 2, 1, 3]
file = 'C-small-attempt0.in'
out = 'C-out.txt'

def method(r, k, l):
    ans = 0
    for i in range(r):
        slots_left = k
        groups_on = 0
        while slots_left > 0 and slots_left >= l[0]:
            ans = ans + l[0]
            slots_left = slots_left - l[0]
            l.append(l[0])
            l = l[1:]
            groups_on = groups_on + 1
            if groups_on >= len(l):
                break
    return ans

def run():
    foo = open(file, 'r+')
    bar = open(out, 'w')
    n = int(foo.readline())
    print n
    for i in range(n):
        info = foo.readline()
        info = info.split(' ')
        list = foo.readline()
        list = list.split(' ')
        list[len(list)-1] = list[len(list)-1][:-1] #gets rid of newline char in last element
        for j in range(len(list)):
            list[j] = int(list[j])
        print info
        print list
        ans = method(int(info[0]), int(info[1]), list)
        print ans
        o ='Case #'+str((i+1))+': '+str(ans)
        print o
        bar.write(o)
        bar.write('\n')
    bar.close()

if __name__ == '__main__':
    print method(5,5,t)
    run()