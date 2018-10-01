import copy

# Given X1, ..., Xn

# DP? N-partite matching?

# Draw an edge between

# For each point in the square, try each of the 12
# letters, extending them so that the set of cubes
# with that letter form a rectangle. Then DP?

# DP: Already built rectangle for first k characters.
# And this is the current maze. k*25^2*25^{}

def no_question_marks(maze):
    for row in maze:
        if '?' in row: return False
    return True

def check_bad(x, maze, x1, x2, y1, y2):
    for i in range(x1, x2+1):
        for j in range(y1,y2+1):
            if maze[i][j] != '?' and maze[i][j] != x: return False

    return True

def DP(maze, letters_to_place):
#    for row in maze: print("".join(row))
#    print(letters_to_place)

    if len(letters_to_place) == 0:
        if no_question_marks(maze): return maze
        else: return False

    current_letter = letters_to_place[0]
    letters_left = letters_to_place[1:]

    # find top left letter, and top right letter, and try and extend past that
    top_left_x = -1
    top_left_y = -1
    for i in range(len(maze)):
        if (top_left_x != -1): break
        for j in range(len(maze[0])):
            if maze[i][j] == current_letter:
                top_left_x = i
                top_left_y = j
                break

    # find top left letter, and top right letter, and try and extend past that
    # TODO: MAKE MORE EFFICIENT
    bot_right_x = -1
    bot_right_y = -1
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == current_letter:
                bot_right_x = i
                bot_right_y = j

    if (not check_bad(current_letter, maze, top_left_x, bot_right_x, top_left_y, bot_right_y)): return False

    # find minimum x_new which works
    top_left_x_new_start = top_left_x
    while (True):
        if (top_left_x_new_start < 0): break
        if (maze[top_left_x_new_start][top_left_y] != '?' and maze[top_left_x_new_start][top_left_y] != current_letter): break
        top_left_x_new_start -= 1
    top_left_x_new_start += 1

    for top_left_x_new in range(top_left_x_new_start,top_left_x+1):
        top_left_y_new_start = top_left_y
        #print(top_left_y_new_start)
        while (top_left_y_new_start >= 0 and check_bad(current_letter, maze, top_left_x_new, top_left_x, top_left_y_new_start, top_left_y)): top_left_y_new_start -= 1
        top_left_y_new_start += 1

        for top_left_y_new in range(top_left_y_new_start, top_left_y+1):
            bot_right_x_new_start = bot_right_x
            while (bot_right_x_new_start < len(maze) and check_bad(current_letter, maze, bot_right_x, bot_right_x_new_start, bot_right_y, bot_right_y)): bot_right_x_new_start += 1
            bot_right_x_new_start -= 1

            for bot_right_x_new in range(bot_right_x_new_start, bot_right_x-1,-1):
                bot_right_y_new_start = bot_right_y
                while (bot_right_y_new_start < len(maze[0]) and check_bad(current_letter, maze, bot_right_x, bot_right_x_new, bot_right_y, bot_right_y_new_start)): bot_right_y_new_start += 1
                bot_right_y_new_start -= 1

                for bot_right_y_new in range(bot_right_y_new_start, bot_right_y-1,-1):
                    new_maze = copy.deepcopy(maze)
                    works = True

                    # fill in rectangle in new range
                    for i in range(top_left_x_new,bot_right_x_new+1):
                        if not works: break
                        for j in range(top_left_y_new, bot_right_y_new+1):
                            #for row in new_maze: print(row)
                            #print(current_letter,i,j, top_left_x_new, top_left_y_new, bot_right_x_new, bot_right_y_new)
                            if (new_maze[i][j] != '?' and new_maze[i][j] != current_letter):
                                works = False
                                break
                            new_maze[i][j] = current_letter

                    if works:
                        recurse = DP(new_maze,letters_left)
                        if (recurse != False): return recurse

    return False

T = int(input(""))

for test_case in range(1,T+1):
    (R,C) = [int(x) for x in input("").split()]

    letters_in_maze = []

    maze = []
    for row in range(R):
        maze.append(list(input("")))
        for x in maze[row]:
            if x != '?' and x not in letters_in_maze: letters_in_maze.append(x)

    print("Case #%d:" % (test_case))
    for row in DP(maze, tuple(letters_in_maze)): print("".join(row))