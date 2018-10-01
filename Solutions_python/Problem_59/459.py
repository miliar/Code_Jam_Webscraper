#!/usr/bin/python

cases=int(raw_input())


for case in xrange(cases):
  N, M = map(int, raw_input().rstrip().split())
  paths=[]
  for n in xrange(N):
    paths.append(raw_input().rstrip().lstrip('/').split('/'))

  sum=0

  for m in xrange(M):
    l=raw_input().rstrip().lstrip('/').split('/')
    for i in xrange(len(l)):
      if not l[:i+1] in paths:
        paths.append(l[:i+1])
        sum+=1

  print 'Case #%d: %d'%(case+1,sum)
