#!/usr/bin/python

import sys

import in_out

def findCommon(s):
  res = list( filter((lambda x: x in s[1]), s[0]) ) 
  #print res
  return res

def main(argv):
  _in_out = in_out.InOut(argv[1])
  T = _in_out.getT()
  _T = 1

  #_T = 1
  while _T <= T:
    s = []
    r = []
    r.append(_in_out.getLineAsInt())
    a = []
    a.append([])
    for i in range(0, 4):
      a[0].append([])
      row = _in_out.getLineAsString()
      row = row.split(" ")
      for _row in row:
        a[0][i].append(int(_row))
      if r[0] == i+1:
        s.append(a[0][i])
    r.append(_in_out.getLineAsInt())
    a.append([])
    for i in range(0, 4):
      a[1].append([])
      row = _in_out.getLineAsString()
      row = row.split(" ")
      for _row in row:
        a[1][i].append(int(_row))
      if r[1] == i+1:
        s.append(a[1][i])
    #print r
    #print a
    #print s

    res = findCommon(s)
    if len(res) > 1:
      _in_out.putString(_T, "Bad magician!")
    elif len(res) == 0:
      _in_out.putString(_T, "Volunteer cheated!")
    else:
      _in_out.putInt(_T, res[0])

    _T = _T + 1

  return True

if __name__ == "__main__":
  in_out.checkArgs(sys.argv)
  main(sys.argv)

