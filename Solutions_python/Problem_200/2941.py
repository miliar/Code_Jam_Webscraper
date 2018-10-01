#!/usr/bin/python

def is_tidy(N):
  for i in range(1, len(N)):
    if N[i] < N[i-1]:
      return False
  return True

def minus_one(N):
  i = len(N) - 1
  result = list(N)

  while i >= 0:
    result[i] = chr((ord(result[i]) - ord('0') - 1)%10 + ord('0'))
    if result[i] is not '9':
      break
    i -= 1

  return ''.join(result)

def solution(N):
  i = len(N) - 1
  result = N
  while i >= 1:
    if result[i - 1] > result[i]:
      result = minus_one(result[:i]) + '9'*(len(N) - i)
    i -= 1
  return result.lstrip('0')

def main():
  T = int(input())
  for i in range(1, T+1):
    print('Case #{}: {}'.format(i, solution(input())))

if __name__ == '__main__':
  main()
