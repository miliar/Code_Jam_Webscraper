#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

#RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP

# Input
  	
# Output
 
# 2
# 3
# .10
# 0.1
# 10.
# 4
# .11.
# 0.00
# 01.1
# .10.
# 	Case #1:
# 0.5
# 0.5
# 0.5
# Case #2:
# 0.645833333333
# 0.368055555556
# 0.604166666667
# 0.395833333333

f = open(sys.argv[1])
nb_case = int(f.readline())
for i in range(nb_case):
    response = []
    game = []
    nb_player = int(f.readline())
    for n in range(nb_player):
        game.append(f.readline())

    wp = []
    for n in range(nb_player):
        wp.append((float(game[n].count("1"))/float(nb_player - game[n].count("."))))

    owp = []
    for n in range(nb_player):
        sum_other = 0.0
        for j in range(len(game[n])-1):
            if game[n][j] == "1":
                sum_other += float(game[j].count("1"))/float(nb_player - game[j].count(".") - 1)
            elif game[n][j] == "0":
                sum_other += float(game[j].count("1")-1)/float(nb_player - game[j].count(".") - 1)
        owp.append(float(sum_other/float(nb_player - game[n].count("."))))
        
    oowp = []
    for n in range(nb_player):
        sum_other = 0.0
        for j in range(len(game[n])-1):
            if game[n][j] != ".":
                sum_other += owp[j]
        oowp.append(float(sum_other/float(nb_player - game[n].count("."))))
    
    for n in range(nb_player):
        response.append(0.25 * wp[n] + 0.50 * owp[n] + 0.25 * oowp[n])

    print("Case #" + str(i+1) + ":")
    for r in response:
        print(str(r))
    
