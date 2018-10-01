def main():
   N = input()
   n = sorted(map(float, raw_input().split()))
   k = sorted(map(float, raw_input().split()))
   cheatscore = 0
   for attempt in xrange(1, N+1):
      cn = sorted(n)[-attempt:]
      ck = sorted(k)[:attempt]
      success = attempt
      for naomi, ken in zip(cn, ck):
         if naomi < ken:
            success = cheatscore
      cheatscore = success
   rulescore = 0
   k = set(k)
   for naomi in n:
      smallest = 2
      for ken in k:
         if ken > naomi and ken < smallest:
            smallest = ken
      if smallest == 2:
         rulescore += 1
      else:
         k.remove(smallest)
   return "%s %s" % (cheatscore, rulescore)

T = input()
for i in xrange(T):
   print "Case #%s: %s" % (i+1, main())
