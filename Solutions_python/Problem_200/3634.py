def problemb(n):
          c = 0
          f = 0
          pmin = -1
          for i,k in zip(n,n[1:]):
              if i < k:
                  pmin = c
              if k < i:
                  #non increasing found
                  f = 1
                  break
              c += 1
          if f:
              #how remaining digits to 9
              l = len(n)-pmin-2
              r = n[:pmin+1] + str(int(n[pmin+1])-1) + l*'9'
          else:
              r = n

          return r

def main():
    for c in range(1,input()+1):
        print "Case #%s:"%c,problemb(raw_input()).lstrip('0')

if __name__ == '__main__':
    main()
