import sys
words = []

def compute_exp(prob_succ, rem_keystrokes, pw_len):
  return prob_succ*rem_keystrokes + (1-prob_succ)*(rem_keystrokes+pw_len+1)

t = int(sys.stdin.readline())

for i in range(t):
  line = sys.stdin.readline().split()
  a = int(line[0])
  b = int(line[1])
  probs = map(float, sys.stdin.readline().split())

  prob_succ = [1]
  exp_strokes = [b+1]
  for x in range(1, a+1):
    prob_succ.append(prob_succ[x-1]*probs[x-1])
    exp_strokes.append(min(compute_exp(prob_succ[x-1], b-x+3, b), compute_exp(prob_succ[x], b-x+1, b)))

  # print prob_succ
  # print exp_strokes

  print "Case #%u: %.6f" % (i+1, min(exp_strokes[a], b+2))
