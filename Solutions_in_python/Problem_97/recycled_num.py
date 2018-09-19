import sys
import itertools
outfile = open('num.out', 'w')
cache = {}

def f1(seq):
   set = {}
   map(set.__setitem__, seq, [])
   return set.keys()

def getrecycled(num):
   cnt = 0
   rec = []
   const_len = len(num)
   while cnt < len(num):
      num = num[-1:] + num[:-1]
      if (len(str(int(num))) == const_len):
         rec.append(int(num))
      cnt += 1
   return rec

def prepare_cache(in_num,b_num):
   tryout = []
   for num in xrange(in_num,b_num + 1):
      if not cache.has_key(num):
         get_nums = sorted(f1(getrecycled(str(num))))
         if len(get_nums) < 2:
            cache[num] = []
         else:
            cache[num] = get_nums
      j = itertools.combinations(itertools.ifilter(lambda x: x <= b_num and x >= in_num,cache[num]),2)
      for x in j:
         if x not in tryout:
            tryout.append(x)
   return len(tryout)

def calc_recycled(a,b):
   if len(a) != len(b):
      return 0
   return prepare_cache(int(a),int(b))

def main(argv=None):
    if not argv:
        argv = sys.argv[1:]
    filename = argv[0] if argv else 'C-small-attempt0.in'
    f = open(filename)
    numCases = int(f.readline())
    for caseNo in xrange(1, numCases+1):
       nums = f.readline().strip().split(' ')
       st = calc_recycled(nums[0],nums[1])
       outfile.write('Case #{0}: {1} \n'.format(caseNo, st))

if __name__ == '__main__':
    main()
