

if __name__ == '__main__':
  T = int(raw_input())

  for i in xrange(1,T+1):
    A1 = int(raw_input()) - 1
    cards1 = [set(int(x) for x in raw_input().split()) for j in xrange(4)]
    A2 = int(raw_input()) -1
    cards2 = [set(int(x) for x in raw_input().split()) for j in xrange(4)]

    select1 = cards1[A1]
    select2 = cards2[A2]

    inter = select1.intersection(select2)

    if len(inter) == 1:
      val = list(inter)[0]
      print "Case #%s: %s" % (i, val)
    elif len(inter) == 0:
      print "Case #%s: Volunteer cheated!" % i
    else:
      print "Case #%s: Bad magician!" % i
    
