#!/usr/bin/python


def mag(N):
    count = 0
    while N >= 10:
        N = N // 10
        count += 1
    return count


def rev(N):
    return int(str(N)[::-1])


def cal(a, b):
    diff = b-rev(a)
    ls = diff % pow(10, mag(b)+1-(mag(b)+1)//2)
    ms = diff//pow(10, mag(b)+1-(mag(b)+1)//2)
    #print('ls %d rev(ms) %d' % (ls, rev(ms)))
    res = b-a
    if rev(a+ls)+rev(ms) == b:
        r = ls+1+rev(ms)
        if r < res: res = r
    if rev(rev(a+ls)+rev(ms)) == b:
        r = ls+1+rev(ms)+1
        if r < res: res = r

    diff = b-rev(a)
    ls = diff % pow(10, mag(b)+1-(mag(b)+1)//2)
    ms = diff//pow(10, mag(b)+1-(mag(b)+1)//2)
    if rev(a+rev(ms))+ls == b:
        r = rev(ms)+1+ls
        if r < res: res = r

    return res

T = int(input())

for t in range(1, T+1):
    N = int(input())
    now = 1
    count = 1
    for i in range(1, mag(N)+1):
        count += cal(now, pow(10, i)-1)+1
        now = pow(10, i)
    count += cal(now, N)
    print('Case #%d: %d' % (t, count))
