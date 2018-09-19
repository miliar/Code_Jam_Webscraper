#! /usr/bin/python3

def main(inFileName):
  with open(inFileName, 'r') as inFile:
    T = int(inFile.readline())
    for t in range(T):

      first = int(inFile.readline().strip("\n"))
      arr1 = [int(x) for x in inFile.readline().strip("\n").split()]
      arr2 = [int(x) for x in inFile.readline().strip("\n").split()]
      arr3 = [int(x) for x in inFile.readline().strip("\n").split()]
      arr4 = [int(x) for x in inFile.readline().strip("\n").split()]

      second = int(inFile.readline().strip("\n"))
      arr5 = [int(x) for x in inFile.readline().strip("\n").split()]
      arr6 = [int(x) for x in inFile.readline().strip("\n").split()]
      arr7 = [int(x) for x in inFile.readline().strip("\n").split()]
      arr8 = [int(x) for x in inFile.readline().strip("\n").split()]

      arra = []
      arra.append(arr1)
      arra.append(arr2)
      arra.append(arr3)
      arra.append(arr4)

      arrb = []
      arrb.append(arr5)
      arrb.append(arr6)
      arrb.append(arr7)
      arrb.append(arr8)

      sel1 = arra[first-1]
      sel2 = arrb[second-1]

      card = 0
      ans = ""

      for each in sel1:
        if each in sel2:
          if card == 0:
            card = each
          else:
            ans = "Bad magician!"
            break
      else:
        if card == 0:
          ans = "Volunteer cheated!"
        else:
          ans = str(card)

      print("Case #{0}: {1}".format(t+1, ans))    

def algo(C, I, P):
  pass

if __name__ == "__main__":
  import sys
  if len(sys.argv) == 2:
    main(sys.argv[1])
