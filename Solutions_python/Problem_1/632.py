def recur(engineIndex, keywordIndex, y):
    global Y, optimalList, Q, S, engines, keywords;

    # cut the branch
    if y > optimalList[keywordIndex]:
        return;
    else:
        optimalList[keywordIndex] = y;
    # update if better solution, and return
    if keywordIndex >= Q:        
        if Y > y:
            Y = y;
        return;

    # if the recur is too deep, quit
    if y >= Y:
        return;
    
    if engines[engineIndex] == keywords[keywordIndex]:
        #we have to change the search engine
        #try every engine except for the current one
        for s in range(0, S):
            if s != engineIndex:
                recur(s, keywordIndex+1, y+1);
    else:
        # stay at the search engine
        recur(engineIndex, keywordIndex+1, y);        



# open the input file
fin = open("A-small-attempt1.in", 'r');
# open the output file
fout = open("A.out", 'w');

# number of cases
N = fin.readline();
N = int(N.strip());


# loop for the number of cases
for n in range(0, N):
    # number of search engines
    S = fin.readline();
    S = int(S.strip());

    
    # read and save the engine names
    engines = [];
    for s in range(0, S):
        temp = fin.readline();
        temp = temp.strip();
        engines.append(temp);

    # number of keywords
    Q = fin.readline();
    Q = int(Q.strip());


    #read and save the keywords
    keywords = [];
    for q in range(0, Q):
        temp = fin.readline();
        temp = temp.strip();
        keywords.append(temp);

    # number of search engine switch
    Y = 1001;

    # memoization
    optimalList = [1001]*(Q+1);

    # solve the problem
    for s in range(0, S):
        recur(s, 0, 0);

    # write the answer
    fout.write('Case #' + str(n+1) + ': ' + str(Y) + '\n');



# close the input file
fin.close();
# close the output file
fout.close();
