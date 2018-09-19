{
 "metadata": {
  "name": "D"
 },
 "nbformat": 3,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": true,
     "input": [
      "def readline_ints():",
      "    return [int(num) for num in fin.readline().strip().split()]"
     ],
     "language": "python",
     "outputs": [],
     "prompt_number": 2
    },
    {
     "cell_type": "code",
     "collapsed": true,
     "input": [
      "import fractions, math",
      "",
      "def find_me(map, H, W):",
      "    for y in range(H):",
      "        for x in range(W):",
      "            if map[y][x] == 'X':",
      "                return (y*2)-1,(x*2)-1",
      "",
      "def pythag(x, y):",
      "    return math.sqrt((x**2) + (y**2))"
     ],
     "language": "python",
     "outputs": [],
     "prompt_number": 11
    },
    {
     "cell_type": "code",
     "collapsed": true,
     "input": [
      "def count_reflections(map, H, W, D):",
      "    roomheight, roomwidth = (H-2)*2, (W-2)*2",
      "    D *= 2",
      "    me_y, me_x = find_me(map, H, W)",
      "    print(\"me\", me_x, me_y, \"room\", roomheight, roomwidth, \"D\", D, \"...\")",
      "    cardinal_reflections = 0",
      "    if me_y*2 <= D:  # North",
      "        cardinal_reflections += 1",
      "        #print(\"N\")",
      "    if me_x*2 <= D:  # West",
      "        cardinal_reflections += 1",
      "        #print(\"W\")",
      "    if (roomheight-me_y)*2 <= D:  # South",
      "        cardinal_reflections += 1",
      "        #print(\"S\")",
      "    if (roomwidth-me_x)*2 <= D:  # East",
      "        cardinal_reflections += 1",
      "        #print(\"E\")",
      "    ",
      "    reflection_angles = []",
      "    ",
      "    visible_heights = math.ceil(D/roomheight)",
      "    visible_widths = math.ceil(D/roomwidth)",
      "    print(\"can see rooms\", visible_heights, visible_widths)",
      "    ",
      "    for rooms_down in range(-visible_heights, visible_heights+1):",
      "        for rooms_across in range(-visible_widths, visible_widths+1):",
      "            if 0 in (rooms_down, rooms_across):",
      "                continue",
      "            reflection_y_dist = rooms_down * roomheight",
      "            #print(reflection_y_dist)",
      "            if rooms_down % 2 == 1:",
      "                reflection_y_dist += me_y - (roomheight - me_y)",
      "            reflection_x_dist = rooms_across * roomwidth",
      "            #print(reflection_x_dist)",
      "            if rooms_across % 2 == 1:",
      "                reflection_x_dist += me_x - (roomwidth - me_x)",
      "            ",
      "            ",
      "            if pythag(reflection_x_dist, reflection_y_dist) > D:",
      "                continue",
      "            ",
      "            angle = fractions.Fraction(reflection_x_dist, reflection_y_dist)",
      "            reflection_dir = (angle, (rooms_down > 0))",
      "            if any(x == reflection_dir for x in reflection_angles):",
      "                continue",
      "            reflection_angles.append(reflection_dir)",
      "            #print(rooms_across, rooms_down,\"|\", reflection_x_dist, reflection_y_dist)",
      "    ",
      "    return cardinal_reflections + len(reflection_angles)"
     ],
     "language": "python",
     "outputs": [],
     "prompt_number": 37
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "# Update this with the filename",
      "fname = \"D-small-attempt0\"",
      "with open(fname+\".in\",\"r\") as fin, open(fname+\".out\",\"w\") as fout:",
      "",
      "    numcases = readline_ints()[0]",
      "    print(numcases, \"cases\")",
      "    ",
      "    for caseno in range(1, numcases+1):",
      "        # Code goes here",
      "        H, W, D = readline_ints()",
      "        map = [fin.readline().strip() for h in range(H)]",
      "        ",
      "        result = count_reflections(map, H, W, D)",
      "        ",
      "        outstr = \"Case #%d: %d\" % (caseno, result)",
      "        fout.write(outstr + \"\\n\")",
      "        print(outstr)"
     ],
     "language": "python",
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "6 cases",
        "me 1 1 room 2 2 D 2 ...",
        "can see rooms 1 1",
        "Case #1: 4",
        "me 1 1 room 2 2 D 4 ...",
        "can see rooms 2 2",
        "Case #2: 8",
        "me 1 1 room 4 2 D 16 ...",
        "can see rooms 4 8",
        "Case #3: 68",
        "me 5 5 room 10 10 D 8 ...",
        "can see rooms 1 1",
        "Case #4: 0",
        "me 5 1 room 6 8 D 6 ...",
        "can see rooms 1 1",
        "Case #5: 2",
        "me 5 1 room 6 8 D 20 ...",
        "can see rooms 4 3",
        "Case #6: 22"
       ]
      }
     ],
     "prompt_number": 38
    },
    {
     "cell_type": "code",
     "collapsed": true,
     "input": [],
     "language": "python",
     "outputs": []
    }
   ]
  }
 ]
}