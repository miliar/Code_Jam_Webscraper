in_file = 'A-large.in'
out_file = 'A-large.out'

def main():
  f = open(in_file)
  of = open(out_file, 'w')
  case_num = int(f.next())
  for i in range(0, case_num):
    engine_num = int(f.next())
    engines = {}
    for j in range(0, engine_num):
      engines[f.next().strip()] = 0
    query_num = int(f.next())
    switch = 0
    remain = engine_num
    for k in range(0, query_num):
      query = f.next().strip()
      if engines[query] == 0:
        if remain == 1:
          switch = switch + 1
          remain = remain - 1
          for key in engines:
            if key != query:
              engines[key] = engines[key] + 1
              remain = remain + 1
            else:
              engines[key] = engines[key] - 1
        else:  
          engines[query] = engines[query] - 1
          remain = remain - 1    
    of.write("Case #%d: %d\r\n" % (i + 1, switch))
  of.close()  


if __name__ == "__main__" : 
  main()