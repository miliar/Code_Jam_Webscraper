def reversenr(x):
    nr = 0
    while x > 0:
        nr = nr * 10 + (x%10)
        x /= 10

    return nr

def isPal(x):
    if x < 0: return False
    if x < 10: return True

    return x == reversenr(x)

def build(f,to):
   # taken from previous execution with params 1, 10^14
   if f == 1 and to == 100000000000000:
      return [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001L, 10221412201L, 12102420121L, 12345654321L, 40000800004L, 1000002000001L, 1002003002001L, 1004006004001L, 1020304030201L, 1022325232201L, 1024348434201L, 1210024200121L, 1212225222121L, 1214428244121L, 1232346432321L, 1234567654321L, 4000008000004L, 4004009004004L]

   res = []
   i = f
   while i <= to:
      sq = i*i
      if sq > to:
          break
      if isPal(i):
          if isPal(sq): res = res + [sq]
          if i > 10:
             i += (11 - (i%10))
          else:
              i += 1
      else:
          i+= 1

      # print i, isPal(i), isPal(sq)

   return res

def searchlow(arr,x):
    l = 0
    h = len(arr)-1
    while( l <= h ):
        # print "Searching for nr ", x, " l=", l, " h=", h
        med = l + (h-l)/2
        if arr[med] == x: return med
        if arr[med] < x:  l = med+1
        else: h = med-1

    return h

def searchhigh(arr,x):
    l = 0
    h = len(arr)-1
    while( l <= h ):
        # print "Searching for nr ", x, " l=", l, " h=", h
        med = l + (h-l)/2
        if arr[med] == x: return med
        if arr[med] < x:  l = med+1
        else: h = med-1

    return l

def howmany( arr, desde, hasta ):
    # print " hm ", desde, hasta, "  ",
    if desde < 1: desde = 1
    # if hasta > 1000: hasta = 1000
    if desde > hasta:
        tmp = desde
        desde = hasta
        hasta = tmp

    return searchlow(arr,hasta) - searchhigh(arr,desde) + 1

def transform(arr):
    values = raw_input().split()
    A = int( values[0] )
    B = int( values[1] ) 
    # print A, B

    return howmany( arr, A, B )

# main()

tabla = build( 1, 100000000000000 )
# print tabla

n = int( input() )
for i in range(n):
    t = transform(tabla)
    print "Case #"+str(i+1) + ":", t

# print howmany( tabla, 1, 4 )
# print howmany( tabla, 10, 120 )
# print howmany( tabla, 100, 1000 )
# print howmany( tabla, 1, 1000 )
