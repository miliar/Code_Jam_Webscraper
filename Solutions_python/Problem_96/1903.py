def main():
  try:
    f_in = open('B-large.in', 'r')
    f_out = open('output.txt', 'w')
    
    cnt = -1
    for line in f_in:
      cnt += 1
      if cnt == 0:
        continue
      
      elements = line.split()
      
      dancers = int(elements[0])
      surprising = int(elements[1])
      best = int(elements[2])
      
      totals = [ int(n) for n in elements[3:] ]
      
      count = 0
      
      for i in totals:
        triple_best = true_best = i / 3
       
        if i % 3 > 0:
          true_best = triple_best + 1
        
        if true_best >= best:
          count += 1
        
        elif true_best == best - 1:
          if (i % 3 == 0 or i % 3 == 2) and not (triple_best == 0 and i % 3 < 2) and (i != 29):
            if surprising > 0:
              count += 1
              surprising -= 1
      
      f_out.write("Case #%d: %d\n" % (cnt, count))
    
    f_in.close()
    f_out.close()
  except Exception as ex:
    print ex
  
  raw_input ()

if __name__ == '__main__':
  main()