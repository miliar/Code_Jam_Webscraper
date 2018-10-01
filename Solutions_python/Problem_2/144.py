asched = None
bsched = None
acnt = 0
bcnt = 0

def start_atrain(time):
  global asched
  for i in range(len(asched)):
    (s,e) = asched[i]
    if s >= time:
      asched.pop(i)
      start_btrain(e)
      return

def start_btrain(time):
  global bsched
  for i in range(len(bsched)):
    (s,e) = bsched[i]
    if s >= time:
      bsched.pop(i)
      start_atrain(e)
      return

def main():
  global asched, bsched, acnt, bcnt
  nc = int(raw_input())
  for c in range(1,nc+1):
    t = int(raw_input())
    nanb = raw_input()
    na = int(nanb[:nanb.index(" ")])
    nb = int(nanb[nanb.index(" ")+1:])

    asched = [None]*na
    bsched = [None]*nb

    for atrain in range(na):
      sched = raw_input()
      start = 60*int(sched[0:2])+int(sched[3:5])
      end = 60*int(sched[6:8])+int(sched[9:11]) + t
      asched[atrain] = (start,end)

    for btrain in range(nb):
      sched = raw_input()
      start = 60*int(sched[0:2])+int(sched[3:5])
      end = 60*int(sched[6:8])+int(sched[9:11]) + t
      bsched[btrain] = (start,end)

    asched.sort()
    bsched.sort()

    acnt = 0
    bcnt = 0

    while (len(asched) != 0 or len(bsched) != 0):
      try:
        at = asched[0][0]
      except:
        at = 24*60+1
      try:
        bt = bsched[0][0]
      except:
        bt = 24*60+1

      if at < bt:
        acnt += 1
        start_atrain(at)
        pass
      else:
        bcnt += 1
        start_btrain(bt)
        pass

    print "Case #%d: %d %d" % (c,acnt,bcnt)

if __name__ == "__main__":
  main()
