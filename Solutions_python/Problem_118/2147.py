import math

def binary_search(elements, target, low, high):
  mid = (low + high) // 2
  if low > high: 
     return False 
  elif elements[mid] == target:
     return True
  elif target < elements[mid]: 
     return binary_search(elements, target, low, mid-1)
  else: 
      return binary_search(elements, target, mid+1, high)



file = open('fairandsquareinput.txt', 'r')
output = open('fairandsquareoutput.txt', 'w')
t = int(file.readline())

square = [1]

for derp in range (1, 10000000):
    square.append(square[derp-1] + 2*derp + 1)
    
for i in range (1, t+1):
    line = file.readline()
    space = str.find(line, ' ')
    start = int(line[:space])
    end = int(line[space:])
    total = 0
    for number in range (start, end+1):
        high = 10000000-1
        if 2*number<high:
            high = 2*number
        if binary_search(square, number, 0, high):
            test = str(number)
            if test == test[::-1]:
                smaller = int(math.sqrt(number))
                test2 = str(smaller)
                if test2==test2[::-1]:
                    total = total+1
    towrite = "Case #" + str(i) + ": " + str(total) + "\n"
    output.write(towrite)
file.close()
output.close()
