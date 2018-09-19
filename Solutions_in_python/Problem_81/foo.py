#!/usr/bin/python
import sys

def calc_owp(mat, i, forbidden_index=-1):
  all = 0.0
  sum = 0.0
  if i == forbidden_index:
    return 0.0
  for x in xrange(len(mat)):
    if x == forbidden_index or mat[i][x] == ".":
      continue
    all += 1
    if mat[i][x] == "1":
      sum += 1
  return sum/float(all)
    

def calc(mat):
  #  RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
  OWP_mat = []
  for i in xrange(len(mat)):
    OWP_mat.append([])
    for j in xrange(len(mat)):
      OWP_mat[-1].append(calc_owp(mat, i, j))

  OWP_vec = []
  for i in xrange(len(mat)):
    sum = 0.0
    ddd = 0
    for j in xrange(len(mat)):
      if i == j:
        continue
      if mat[i][j] != ".":
        sum += OWP_mat[j][i]
        ddd += 1
    OWP_vec.append(float(sum)/ddd)

  OOWP_vec = []
  for i in xrange(len(mat)):
    sum = 0.0
    ddd = 0
    for j in xrange(len(mat)):
      if i == j:
        continue
      if mat[i][j] != ".":
         sum += OWP_vec[j]
         ddd += 1
    OOWP_vec.append(float(sum)/ddd)
  
  ret_s = ""
  for i in xrange(len(mat)):
    val = 0.25*calc_owp(mat, i) + 0.5*OWP_vec[i] + 0.25*OOWP_vec[i]
    ret_s += "\n" + str(val) 
  
  return ret_s

def main(filename):
  f = file(filename)
  n = int(f.readline())
  for case in xrange(1, n+1):
    dim = int(f.readline())
    mat = []
    for i in xrange(dim):
      mat.append(list(f.readline().rstrip('\n')));
    print "Case #%d:%s" % (case, calc(mat))

if __name__ == "__main__":
  main(sys.argv[1])
