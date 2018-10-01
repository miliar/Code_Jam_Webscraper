import sys

class Walkway:
    def __init__(self, start, end, speed):
        self.start = start
        self.end = end
        self.speed = speed
        
    def length(self):    
        return self.end - self.start
        
    def __str__(self):
        return "[" + str(self.start) + "," + str(self.end) + "]" + "@" + str(self.speed)

numcases = int(sys.stdin.readline())
for casenumber in xrange(1,numcases+1):
    line = sys.stdin.readline().rstrip("\r\n")
    line_elems = line.split(" ")
    
    length_of_corridor = float( line_elems[0] )
    walking_speed = float( line_elems[1] )
    running_speed = float( line_elems[2] )
    run_seconds_remaining = float( line_elems[3] )
    n_walkways = int( line_elems[4] )
    walkways = []
    for i in xrange(0, n_walkways):
        line = sys.stdin.readline().rstrip("\r\n")
        line_elems = line.split(" ")
        new_walkway = Walkway(int(line_elems[0]), int(line_elems[1]), float(line_elems[2]))
        if new_walkway.start < length_of_corridor:
            new_walkway.end = min( new_walkway.end, length_of_corridor )
            walkways.append(new_walkway)
    
    walkways.sort(key=lambda walkway: walkway.start)
    
    
    # So i don't have to worry about joggers/speedwalkers
    if running_speed < walking_speed:
        run_seconds_remaining = 0
        running_speed = walking_speed
    
    # Add fake walkways for the unassisted segments
    new_walkways = []
    lpos = 0   
    for walkway in walkways:
        if walkway.start != lpos:
            fake_walkway = Walkway( lpos, walkway.start, 0.0 )
            new_walkways.append(fake_walkway)
        new_walkways.append(walkway)
        lpos = walkway.end
    if lpos != length_of_corridor:
        fake_walkway = Walkway( lpos, length_of_corridor, 0.0 )     
        new_walkways.append(fake_walkway)
         
    walkways = new_walkways

    num_seconds = 0
    
    # Travel by slowest->fastest
    walkways_by_speed = sorted(walkways, key=lambda walkway: walkway.speed)

    for walkway in walkways_by_speed:
    
        current_position = 0
        if run_seconds_remaining > 0:
            effective_speed = running_speed + walkway.speed   
            metres_can_run = effective_speed * run_seconds_remaining
            run_metres = min( walkway.length(), metres_can_run )
            run_seconds = (run_metres / effective_speed)
            current_position += run_metres
            num_seconds += run_seconds
            run_seconds_remaining -= run_seconds
         
        if current_position < walkway.length():
            walk_distance = walkway.length() - current_position
            effective_speed = walking_speed + walkway.speed   
            walk_seconds = walk_distance / effective_speed
            num_seconds += walk_seconds
            current_position = walkway.end

        
    result = str(num_seconds)
    print "Case #%d: %s" % (casenumber, result)



