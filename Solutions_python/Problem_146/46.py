#!/usr/bin/env python3
# vim:set sw=4 et smarttab:
# Round 1C 2014

import sys
import collections

modulo = 1000000007

def main():
    filein = sys.stdin
    #filein = open('filename.in', 'r')
    line = filein.readline()
    fields = line.split()
    assert len(fields) == 1
    ntc = int(fields[0])

    for tc in range(1, ntc + 1):
        line = filein.readline()
        fields = line.split()
        assert len(fields) == 1
        n = int(fields[0])
        line = filein.readline()
        fields = line.split()
        assert len(fields) == n
        answer = solve(fields)
        print('Case #{0}: {1}'.format(tc, answer))

def solve(cars):
    for car in cars:
        if not valid(car):
            return 0
    for i in range(len(cars)):
        cars[i] = reduce(cars[i])
    first_letters = set()
    last_letters = set()
    middle_letters = set()
    loop_cars = collections.Counter()
    adj = {}
    for car in cars:
        first_letter = car[0]
        if first_letter in middle_letters:
            return 0
        last_letter = car[-1]
        if last_letter in middle_letters:
            return 0
        next_middle_letters = middle_letters.copy()
        for letter in car[1:-1]:
            if letter in middle_letters:
                return 0
            next_middle_letters.add(letter)
        middle_letters = next_middle_letters

        if car[0] == car[-1]:
            loop_cars[car[0]] += 1
        else:
            if first_letter in first_letters:
                return 0
            first_letters.add(first_letter)
            if last_letter in last_letters:
                return 0
            last_letters.add(last_letter)
            assert not first_letter in adj
            adj[first_letter] = last_letter

    answer = 1
    division = 0
    visited = set()
    for letter in adj:
        if letter in visited:
            continue
        if letter in last_letters:
            continue
        visited.add(letter)
        division += 1
        answer_connected = 1
        if loop_cars[letter] > 0:
            answer_connected *= factorial_modulo(loop_cars[letter])
            answer_connected %= modulo
        next_letter = adj[letter]
        while True:
            assert not next_letter in visited
            visited.add(next_letter)
            if loop_cars[next_letter] > 0:
                answer_connected *= factorial_modulo(loop_cars[next_letter])
                answer_connected %= modulo
            if not next_letter in adj:
                break
            next_letter = adj[next_letter]
        answer *= answer_connected
        answer %= modulo
    for letter in adj:
        if not letter in visited:
            return 0
    for letter in loop_cars:
        if loop_cars[letter] > 0 and not letter in visited:
            answer *= factorial_modulo(loop_cars[letter])
            answer %= modulo
            division += 1
    answer *= factorial_modulo(division)
    answer %= modulo
    return answer

def valid(car):
    occured = set()
    for i in range(len(car)):
        if car[i] in occured:
            assert i > 0
            if car[i] != car[i - 1]:
                return False
        occured.add(car[i])
    return True

def reduce(car):
    ret = ''
    for i in range(len(car)):
        if i > 0 and car[i] == car[i - 1]:
            continue
        ret += car[i]
    return ret

def factorial_modulo(n):
    if n == 0:
        return 1
    return n * factorial_modulo(n - 1) % modulo

if __name__ == '__main__':
    main()
