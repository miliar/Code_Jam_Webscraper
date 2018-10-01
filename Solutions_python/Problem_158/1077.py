# Google Code Jam 2015

def fillable(X, R, C):
    if X == 1:
      return True # Gabriel can always fill
    if X > R * C:
      return False
    if R * C % X != 0:
      return False 
    if X == 2:
      if R % 2 and C % 2:
        return False
      return True
    if X == 3:
      if R < 3 and C < 3:
        return False
      if R == 1 or C == 1:
        return False # Richard picks an L piece. Dammit Richard
      if R == 3 or C == 3:
        return True
      assert False # No other 3-cases
    if X == 4:
      if R == 1 or C == 1:
        return False
      if R <= 3 and C <= 3:
        return False
      if (R == 4 and C == 2) or (R == 2 and C == 4):
        return False
      return True


def tests():


  # 3s
  assert fillable(1, 1, 1)
  assert fillable(1, 1, 2)
  assert fillable(1, 1, 4)
  assert fillable(1, 2, 2)
  assert fillable(1, 2, 3)
  assert fillable(2, 4, 1)
  assert fillable(3, 2, 3)
  assert fillable(3, 3, 2)
  assert fillable(4, 3, 4)
  assert not fillable(4, 4, 1)
  assert not fillable(4, 4, 2)
  assert not fillable(4, 2, 4)
  assert fillable(4, 4, 3)
  assert fillable(4, 4, 4)
  assert not fillable(2, 1, 1)
  assert not fillable(2, 3, 3)
  assert not fillable(3, 1, 1)
  assert not fillable(3, 1, 3)
  assert not fillable(3, 2, 1)
  assert not fillable(3, 2, 2)
  assert not fillable(3, 3, 1)
  assert not fillable(3, 4, 2)
  assert not fillable(3, 4, 4)
  assert not fillable(4, 1, 3)
  assert not fillable(4, 2, 2)
  assert not fillable(4, 3, 1)
  assert not fillable(4, 3, 2)
  assert not fillable(4, 3, 2)
  assert not fillable(4, 4, 1)

  # First answer set
  assert fillable(2, 2, 2)

def genwinners(fname):
  s = ""
  lines = open(fname).readlines()[1:]
  casenum = 1
  for l in lines:
    l = l.strip()
    print l.split()
    (X, R, C) = [int(i) for i in l.split()]
    s += "Case #{}: {}\n".format(casenum, "GABRIEL" if fillable(X, R, C) else "RICHARD")
    casenum += 1
  print s
  return s

def test_e2e(fname, correctfname):
  f = open(correctfname)
  myans = genwinners(fname)
  key = "".join(f.readlines())
  print key
  assert myans == key


if __name__ == "__main__":
    tests()
    print "Tests passed."
    test_e2e("testin.txt", "testout.txt.gold")
    infilename = "D-small-attempt1.in"
    downloadsdirectory = "/Users/robertkarl/Downloads/"
    answer = genwinners(downloadsdirectory + infilename)
    outfile = open(downloadsdirectory + "ans.txt", 'w')
    outfile.write(answer)
    outfile.close()

