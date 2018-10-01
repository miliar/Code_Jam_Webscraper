from sys import stdin
from sets import Set
from math import sqrt, ceil, floor

def is_palindrome(num):
  return str(num) == str(num)[::-1] 

def find_palindromes(min_val, max_val):
  palindromes = Set() 
  for val in range(min_val, max_val+1):
    if is_palindrome(val):
      palindromes.add(val)
  return palindromes

def main():
  num_cases = int(stdin.readline())
  endpoints = []
  for case in range(num_cases):
    vals = stdin.readline().split()
    endpoints.append([int(ceil(sqrt(int(vals[0])))), int(floor(sqrt(int(vals[1]))))])
  min_endpoint = min([endpoint[0] for endpoint in endpoints])
  max_endpoint = max([endpoint[1] for endpoint in endpoints])
  cache = find_palindromes(min_endpoint, max_endpoint)
  for i in range(len(endpoints)):
    count = 0;
    for j in range(endpoints[i][0], endpoints[i][1]+1):
      if j in cache:
        if is_palindrome(j**2):
          count += 1
    print 'Case #{}: {}'.format(i+1, count)

if __name__ == '__main__':
  main()
