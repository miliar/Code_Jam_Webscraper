# cd C:/Dropbox/Joe/google_code_jam
filename = '2014_qual_A-small-attempt0'
input = open('C:\\Dropbox\\Joe\\google_code_jam\\{}.in'.format(filename)).read()
input = input.split('\n')
n_cases = int(input[0])
output = ''

from numpy import fromstring, array, minimum, maximum, floor
from pandas import Panel, DataFrame, Series
from datetime import datetime, timedelta
prgm_start = datetime.now()

def str_to_Series(str):
  return Series(fromstring(str, dtype=float, sep=' '))

def reverse_Series(s):
  return Series(array(s)[::-1], index=s.index)

for c in range(n_cases):
  row = c*10 + 1
  guess1 = int(input[row])
  grid1_row1 = str_to_Series(input[row+1])
  grid1_row2 = str_to_Series(input[row+2])
  grid1_row3 = str_to_Series(input[row+3])
  grid1_row4 = str_to_Series(input[row+4])
  guess2 = int(input[row+5])
  grid2_row1 = str_to_Series(input[row+6])
  grid2_row2 = str_to_Series(input[row+7])
  grid2_row3 = str_to_Series(input[row+8])
  grid2_row4 = str_to_Series(input[row+9])
  
  grid1 = DataFrame([grid1_row1, grid1_row2, grid1_row3, grid1_row4])
  grid2 = DataFrame([grid2_row1, grid2_row2, grid2_row3, grid2_row4])
  
  row1 = str_to_Series(input[row + guess1])
  row2 = str_to_Series(input[row + 5 + guess2])
  
  intersection = Series(list(set(row1).intersection(set(row2))))
  if len(intersection) == 1:
    answer = int(intersection[0])
  elif len(intersection) > 1:
    answer = 'Bad magician!'
  elif len(intersection) == 0:
    answer = 'Volunteer cheated!'
  
  result = 'Case #{}: {}'.format(c+1, answer)
  print datetime.now(), '   ', result
  output = output + result + '\n'
#
x = (datetime.now() - prgm_start).total_seconds()
print 'Code run time = {:02.0f}:{:02.0f}:{:06.3f}'.format(floor(x/3600), floor((x%3600)/60), x%60)
with open('{}.txt'.format(filename), 'w') as text_file: text_file.write(output[:-1]) # strip last blank line