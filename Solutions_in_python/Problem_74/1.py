#!/usr/bin/python -tt

import sys
import os
import subprocess

def main():
#  data = file("sample").readlines()
  data = file("A-small-attempt1.in").readlines()

  solution = ""
  n = 1
  for line in data:
    if len(line) < 5:
      x = int(line)
    elif len(line) > 1:
      instructions = ReadLine(line)
      solution += ("Case #" + str(n) + ": " + str(Solve(instructions)) + "\n")
      n += 1

  print (solution)
  file("output", 'w').write(solution)

def Solve(instructions):
  bPos = 1
  oPos = 1
  t = 0

  while len(instructions) > 0:
    nextPusher = NextPusher(instructions)
    nextOButton = NextOButton(instructions)
    nextBButton = NextBButton(instructions)
    buttonPushed = False

    if oPos == nextOButton and nextPusher == 'O':
      buttonPushed = True
    else:
      if oPos < nextOButton: oPos += 1
      elif oPos > nextOButton: oPos -= 1

    if bPos == nextBButton and nextPusher == 'B':
      buttonPushed = True
    else:
      if bPos < nextBButton: bPos += 1
      elif bPos > nextBButton: bPos -= 1

    if buttonPushed:
      instructions.pop(0)

    t += 1

  return t

def ReadLine(line):
  n = int(line[0])
  line = line[2:]

  tokens = line.strip().split(' ')
  instructions = []
  while len(tokens) > 0:
    instructions.insert(len(instructions), [tokens[0],tokens[1]])
    tokens.pop(0)
    tokens.pop(0)

  return instructions

def NextPusher(instructions):
  return instructions[0][0]

def NextOButton(instructions):
  for instruction in instructions:
    if instruction[0] == 'O':
      return int(instruction[1])

def NextBButton(instructions):
  for instruction in instructions:
    if instruction[0] == 'B':
      return int(instruction[1])

def GetAspectRatioProduct(videoStreamInfo, parSubString, darSubString, darTerminator):
    parStart = videoStreamInfo.find(parSubString)
    if (parStart >= 0):
      # get PAR info
      parStart = parStart + len(parSubString)
      parEnd = videoStreamInfo.find('%', parStart)
      parInfo = videoStreamInfo[parStart:parEnd].split(':')
      # get DAR info
      darStart = videoStreamInfo.find(darSubString, parEnd) + len(darSubString)
      darEnd = videoStreamInfo.find(darTerminator, darStart)
      darInfo = videoStreamInfo[darStart:darEnd].split(':')
      # calculate a magic ratio
      return (float(parInfo[0]) / float(parInfo[1])) * (float(darInfo[0]) / float(darInfo[1]))

if __name__ == '__main__':
  main()
