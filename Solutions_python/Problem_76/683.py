if __name__ == '__main__':
  num_of_cases = int(raw_input())
  for case_index in range(num_of_cases):
    num_candies = int(raw_input())
    candies = [int(k) for k in raw_input().strip().split()]
    candies.sort()
    if reduce(lambda x,y: x^y, candies) == 0:
      print "Case #%d: %d" % (case_index+1, reduce(lambda x,y: x+y, candies[1:]))
    else:
      print "Case #%d: NO" % (case_index+1,)
