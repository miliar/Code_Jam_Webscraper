import numpy as np

def small(R,Y,B):
  if B > R+Y:
    return 'IMPOSSIBLE'
  elif R > B+Y:
    return 'IMPOSSIBLE'
  elif Y > R+B:
    return 'IMPOSSIBLE'
  N = R+Y+B
  old_l = np.array([R,Y,B])
  l_order = np.argsort(-old_l)
  l = [old_l[j] for j in l_order]
  print l  
  old_labels = ['R','Y','B']
  labels = [old_labels[j] for j in l_order]

  tmp_l = l
  output = ''
  for i in range(N):
    index = np.argmax(tmp_l)
    output += labels[index]
    l[index] = l[index] - 1
    tmp_l = np.array(l)
    tmp_l[index] = 0
  return output

if __name__ == '__main__':
  inputfile = 'B-small-attempt1.in'
  outputfile = inputfile + '.out'
  f_in = open(inputfile, 'r')
  f_out = open(outputfile, 'w')

  T = int(f_in.readline())
  print T
  for i in range(T):
    N, R, O, Y, G, B, V = [int(x) for x in f_in.readline()[:-1].split()]
    output_string = small(R,Y,B)

    f_out.write('Case #' + str(i+1) + ': ' + output_string + '\n')

  f_in.close()
  f_out.close()
