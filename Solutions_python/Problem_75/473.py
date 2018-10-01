
for case in range(1, int(input()) + 1):

  s = input().split()
  combos, opposed = {}, set()

  for _ in range(int(s.pop(0))):
    a, b, c = s.pop(0)
    combos[a + b] = combos[b + a] = c

  for _ in range(int(s.pop(0))):
    a, b = s.pop(0)
    opposed.update({ a + b, b + a })

  els = []
  for c in s.pop(1):
    els.append(c)

    combo = ''.join(els[-2:])
    if combo in combos:
      els[-2:] = combos[combo]

    if any(els[-1] + c in opposed for c in els[:-1]):
      els = []

  print('Case #%d: [%s]' % (case, ', '.join(els)))
