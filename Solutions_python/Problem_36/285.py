import re

pattern = 'welcome to code jam'
f = open('./C-small-attempt0.in', 'r')
n = int(f.readline())
for x in range(n):
  line = f.readline().replace('\n', '')
  line = re.sub(r'[^w]*(w.*m)[^m]*', r'\1', line)
  if not re.match(r'^w.*e.*l.*c.*o.*m.*e.* .*t.*o.* .*c.*o.*d.*e.* .*j.*a.*m$', line):
    print 'Case #' + str(x + 1) + ': 0000'

  else:
    cnt = 0
    def check(li, pi, arr1, arr2, s):
      global cnt
      #print s
      if pi == len(pattern):
        cnt += 1
        #print cnt
        return
      #print arr1
      #print arr2
      r = 0
      if li == 0 and pi == 0:
        r = len(line) - len(pattern) + 1
      else:
        r = len(line[li - 1:]) - len(pattern[pi - 1:]) + 1
      for i in range(r):
        if line[li + i] == pattern[pi]:
          arr1.append(li + i)
          arr2.append(pi)
          check(li + i + 1, pi + 1, arr1, arr2, s + pattern[pi])
          arr1.pop()
          arr2.pop()

    #print line
    #print pattern
    arr1 = []
    arr2 = []
    s = ''
    check(0, 0, arr1, arr2, s)

    print 'Case #' + str(x + 1) + ': %04d' % cnt

