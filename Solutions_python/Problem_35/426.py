#!/usr/bin/env py3k
"""
Problem

Geologists sometimes divide an area of land into different regions based on where rainfall flows down to. These regions are called drainage basins.

Given an elevation map (a 2-dimensional array of altitudes), label the map such that locations in the same drainage basin have the same label, subject to the following rules.

From each cell, water flows down to at most one of its 4 neighboring cells.
For each cell, if none of its 4 neighboring cells has a lower altitude than the current cell's, then the water does not flow, and the current cell is called a sink.
Otherwise, water flows from the current cell to the neighbor with the lowest altitude.
In case of a tie, water will choose the first direction with the lowest altitude from this list: North, West, East, South.
Every cell that drains directly or indirectly to the same sink is part of the same drainage basin. Each basin is labeled by a unique lower-case letter, in such a way that, when the rows of the map are concatenated from top to bottom, the resulting string is lexicographically smallest. (In particular, the basin of the most North-Western cell is always labeled 'a'.)
Input

The first line of the input file will contain the number of maps, T. T maps will follow, each starting with two integers on a line -- H and W -- the height and width of the map, in cells. The next H lines will each contain a row of the map, from north to south, each containing W integers, from west to east, specifying the altitudes of the cells.

Output

For each test case, output 1+H lines. The first line must be of the form

Case #X:
where X is the test case number, starting from 1. The next H lines must list the basin labels for each of the cells, in the same order as they appear in the input.
Limits

T ? 100;
Small dataset

1 ? H, W ? 10;
0 ? altitudes < 10.
There will be at most two basins.

Large dataset

1 ? H, W ? 100;
0 ? altitudes < 10,000.
There will be at most 26 basins.
"""
from sys import stdin

letters = tuple('#abcdefghijklmnopqrstuvwxyz')

def get_dyx(direction, y, x):
    direction_types = {'N':(y-1,x),'W':(y,x-1),'E':(y,x+1),'S':(y+1,x)}
    return direction_types[direction]

def get_directions(map, size, y, x):
    directions = {}
    for d in ('N', 'W', 'E', 'S'):
        group = get_dyx(d, y, x)
        if (group[0] < 0) or (group[1] < 0):
            directions[d] = 10001
        elif (group[0] + 1) > size[0]:
            directions[d] = 10001
        elif (group[1] + 1) > size[1]:
            directions[d] = 10001
        else:
            directions[d] = map[group[0]][group[1]]
    return directions

def follow_to_sink(map, size, loc, visited):
    (y, x) = loc
    directions = get_directions(map, size, y, x)
    lowest = ['', 10001]
    for direction in ('N', 'W', 'E', 'S'):
        dir_value = directions[direction]
        if dir_value < lowest[1]:
            lowest[1] = dir_value
            lowest[0] = direction
    visited.append((y, x))
    if lowest[0] == '':
        return visited
    next = directions[lowest[0]]
    if next >= map[y][x]:
        return visited
    else:
        return follow_to_sink(map, size, get_dyx(lowest[0], y, x), visited)

def make_labels(map):
    (size, map) = map
    y = 0
    x = 0
    done = []
    letter = '#'
    labels = [['' for i in range(size[1])] for j in range(size[0])]
    for y in range(size[0]):
        for x in range(size[1]):
            cell = map[y][x]
            if (y, x) not in done:
                sink_path = follow_to_sink(map, size, (y, x), [])
                last = sink_path[len(sink_path) - 1]
                sink_letter = labels[last[0]][last[1]]
                if sink_letter == '':
                    letter = letters[letters.index(letter) + 1]
                    sink_letter = letter
                for cell in sink_path:
                    labels[cell[0]][cell[1]] = sink_letter
                done.extend(sink_path)
    retstr = ''
    for line in labels:
        retstr += ' '.join(line) + '\n'
    return retstr.strip()

lines = stdin.readlines()
nomaps = int(lines.pop(0))
maps = []

for mapno in range(nomaps):
    infoline = lines.pop(0)
    (height, width) = [int(i) for i in infoline.split(' ')]
    map = []
    for lineno in range(height):
        line = lines.pop(0)
        map.append([int(i) for i in line.split(' ')])
    maps.append(((height, width), map))

case = 1

for map in maps:
    print('Case #%s:\n%s' % (case, make_labels(map)))
    case += 1