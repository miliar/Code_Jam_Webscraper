#!/usr/bin/python
import optparse
import sys

def light_on_mathy(N, K):
  return ((K + 1) % (2**N)) == 0

def light_on_manual(N, K):
  snappers = [False for n in range(N)]
  for k in range(K):
    # perform single snap
    for n in range(N):
      snappers[n] = not snappers[n]
      if snappers[n]:
        break
  return all(snappers)

parser = optparse.OptionParser()
parser.add_option("--fast", action="store_true", dest="fast")
opts, _ = parser.parse_args()

T = long(sys.stdin.readline())
for t in range(T):
  N, K = map(long, sys.stdin.readline().split(' '))
  on = light_on_mathy(N, K)
  if not opts.fast:
    assert on == light_on_manual(N, K)
  print "Case #%i: %s" % (t+1, "ON" if on else "OFF")