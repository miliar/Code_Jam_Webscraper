def mksample(in_str, out_str):
  return dict(zip(list(in_str), list(out_str)))


case1 = mksample("ejp mysljylc kd kxveddknmc re jsicpdrysi",
                 "our language is impossible to understand")

case2 = mksample("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                 "there are twenty six factorial possibilities")

case3 = mksample("de kr kd eoya kw aej tysr re ujdr lkgc jv",
                 "so it is okay if you want to just give up")

case4 = mksample("a zoo", "y qee")

total_samples = {}
total_samples.update(case1)
print total_samples['k']
total_samples.update(case2)
total_samples.update(case3)
total_samples.update(case4)


total_samples['q'] = 'z'
total_samples['o'] = 'k'
total_samples['\n'] = ''
print total_samples

"""
print len(total_samples)
x = total_samples.keys()
x = sorted(x)
all_chars = list("abcdefghijklmnopqrstuvwxyz")
for char in x:
  #print char, total_samples[char]
  if total_samples[char] in all_chars:
    all_chars.remove(total_samples[char])
print all_chars
for x,y in total_samples.iteritems():
  print x,y
"""
INPUT_FILENAME = "A-small-attempt2.in"
OUTPUT_FILENAME = "A-small-attempt2.out"

if __name__ == "__main__":
  with open(INPUT_FILENAME, 'r') as f:
    with open(OUTPUT_FILENAME, 'w') as of:
      no_of_cases = int(f.readline())
      for line_no in range(no_of_cases):
        line = f.readline()
        output = map(lambda x: total_samples[x], line)
        of.write("Case #%d: %s\n" % (line_no+1, ''.join(output)))    
