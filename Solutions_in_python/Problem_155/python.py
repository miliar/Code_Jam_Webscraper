import math
global maxShy, TotalPeople;
array = [];
with open("input.txt", "r") as ins:
    for line in ins:
        array.append(line);

numberOfTests = int(array[0]);

for j in range(1, numberOfTests+1):
    words = array[j].split();
    maxShy = int(words[0]);
    audience = words[1];
    print (audience);
    TotalPeople = 0;
    missing = 0;
    for i in range(0, maxShy+1):
       # print('i is : '+ str(i));
        peopleWithCurrentShy = int(audience[i]);
        if  (TotalPeople < i and peopleWithCurrentShy>0):
            missing = missing + (i-TotalPeople);
            TotalPeople = TotalPeople+missing + peopleWithCurrentShy;
            #print('couldnt, missing '+ str(missing));
            if TotalPeople > maxShy: break;
        else:
            TotalPeople = TotalPeople + peopleWithCurrentShy;
        
    #if missing==0: print('missing '+ str(0));
      
    with open('output.txt', 'a') as the_file:
            str1 = 'Case #' + str(j) + ': ' + str(missing) + '\n';
            the_file.write(str1)
