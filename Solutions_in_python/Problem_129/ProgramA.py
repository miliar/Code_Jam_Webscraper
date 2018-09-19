#import codejam as gcj

#MOD = 1000002013

#T = gcj.read_input('i')
#for t in range(T):
#    N, M = gcj.read_input('i i')
#    trips_to_make = []
#    for ii in range(M): trips_to_make.append(gcj.read_input('i[]'))
#    trips_to_make.sort()
#    saving = 0
#    trips_in_prog = []
#    for new_start, new_end, new_people in trips_to_make:
#        trips_in_prog = filter(lambda tup: tup[1] >= new_start, trips_in_prog)
#        trips_in_prog.sort(reverse=True)
#        new_trips = []
#        while new_people > 0 and trips_in_prog != []:
#            old_start, old_end, old_people = trips_in_prog.pop()
#            if new_end > old_end:
#                swaps = old_people if (old_people < new_people) else new_people
#                new_people -= swaps
#                saving_per_swap = ((new_end - old_end) * (new_start - old_start))
#                saving += ((saving_per_swap * swaps) % MOD)
#                if old_people - swaps > 0:
#                    #new_trips.append([new_start, old_end, old_people - swaps])
#                    new_trips.append([old_start, old_end, old_people - swaps])
#                new_trips.append([new_start, old_end, swaps])
#                new_trips.append([old_start, new_end, swaps])
#            else: 
#                new_trips.append([old_start, old_end, old_people])
#        if new_people > 0:
#            new_trips.append([new_start, new_end, new_people])
#        trips_in_prog += new_trips
#        
#    print "Case #%d:" % (t + 1), saving

import codejam as gcj

MOD = 1000002013

T = gcj.read_input('i')
for t in range(T):
    N, M = gcj.read_input('i i')
    trips_to_make = []
    for ii in range(M): trips_to_make.append(gcj.read_input('i[]'))
    trips_to_make.sort()
    saving = 0
    while trips_to_make != []:
        trips_to_make.sort(key = lambda tup: tup[0], reverse = True)
        new_start, new_end, new_people = trips_to_make.pop()
        if new_start == new_end:
          #  print trips_to_make, new_start, new_end, new_people
            assert(False)
            continue
        poss_swap_people = filter(lambda tup: tup[0] > new_start and tup[0] <= new_end and tup[1] > new_end, trips_to_make)
   #     print new_start, new_end, new_people
    #    print poss_swap_people
        if poss_swap_people != []:
            poss_swap_people.sort(key = lambda tup: tup[1]) 

            while new_people > 0 and poss_swap_people != []:
                old_start, old_end, old_people = poss_swap_people.pop()
                if old_end > new_end:
                    swaps = old_people if (old_people < new_people) else new_people
                    new_people -= swaps
                    saving_per_swap = ((old_end - new_end) * (old_start - new_start))
                    saving += ((saving_per_swap * swaps) % MOD)
                    trips_to_make.remove([old_start, old_end, old_people])
                    if old_people - swaps > 0:
                        trips_to_make.append([old_start, old_end, old_people - swaps])
                    trips_to_make.append([new_start, old_end, swaps])
                    if old_start != new_end:
                        trips_to_make.append([old_start, new_end, swaps])
                else: 
                    assert(False)
                    new_trips.append([old_start, old_end, old_people])

            if new_people > 0: trips_to_make.append([new_start, new_end, new_people])
        
    print "Case #%d:" % (t + 1), saving
