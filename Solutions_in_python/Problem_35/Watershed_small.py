# GLOBAL VARIABLES #
HEIGHT = 0;
WIDTH = 0;
INIT_CHAR = '-';

basin = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];

next_basin = -1;

least = 99999;

LARGEST = 99999;
DIRECTION_NORTH = 1;
DIRECTION_WEST = 2;
DIRECTION_EAST = 3;
DIRECTION_SOUTH = 4;
SINK = 5;

###################################################################################################

def getNorth(map, row, column):
    if (0 != row):
        return map[row -1][column];
    else:
        return LARGEST;


def getWest(map, row, column):
    if (0 != column):
        return map[row][column -1];
    else:
        return LARGEST;


def getSouth(map, row, column):
    if ((HEIGHT-1) != row):
        return map[row + 1][column];
    else:
        return LARGEST;


def getEast(map, row, column):
    if ((WIDTH-1) != column):
        return map[row][column + 1];
    else:
        return LARGEST;


def getDirection(map, row, column):
    cell_value = map[row][column];
    north = getNorth(map, row, column);
    east = getEast(map, row, column);
    west = getWest(map, row, column);
    south = getSouth(map, row, column);
    #print "---------------[%d][%d][%d][%d]" % (north, east, west, south);

    if cell_value == least:
        return SINK;
    elif( (north <= cell_value) and (north <= west) and (north <= east) and (north <= south) ):
        return DIRECTION_NORTH;
    elif ( (west <= cell_value) and (west <= north) and (west <= east) and (west <= south) ):
        return DIRECTION_WEST;
    elif ( (east <= cell_value) and (east <= north) and (east <= west) and (east <= south) ):
        return DIRECTION_EAST;
    elif ( (south <= cell_value) and (south <= north) and (south <= west) and (south <= east) ):
        return DIRECTION_SOUTH;
    else:
        return SINK;


def getDirectionText(value):
    if value == DIRECTION_NORTH:
        return "NORTH";
    elif value == DIRECTION_EAST:
        return "EAST";
    elif value == DIRECTION_WEST:
        return "WEST";
    elif value == DIRECTION_SOUTH:
        return "SOUTH";
    elif value == SINK:
        return "SINK";


def setBasins(map, row, column, previous_operation):
    global next_basin;

    #print "Output map[%d,%d] ---> " %(row,column),out_map[row][column] ;

    if out_map[row][column] == '-':
        direction = getDirection(map,row,column);

        #print direction,previous_operation;
        if(((previous_operation==DIRECTION_NORTH) and (direction==DIRECTION_SOUTH)) or ((previous_operation==DIRECTION_SOUTH) and (direction==DIRECTION_NORTH)) or ((previous_operation==DIRECTION_EAST) and (direction==DIRECTION_WEST)) or (previous_operation==DIRECTION_WEST) and (direction==DIRECTION_EAST)):
            direction = SINK;

        #print direction,previous_operation;

        if DIRECTION_NORTH == direction:
            #print "Going North";
            out_map[row][column] = setBasins(map, row-1, column,direction);
            #print "North -> ", out_map;
        elif DIRECTION_WEST == direction:
            #print "Going West";
            out_map[row][column] = setBasins(map, row, column-1,direction);
            #print "West -> ", out_map;
        elif DIRECTION_EAST == direction:
            #print "Going East";
            out_map[row][column] = setBasins(map, row, column+1,direction);
            #print "East -> ", out_map;
        elif DIRECTION_SOUTH == direction:
            #print "Going South";
            out_map[row][column] = setBasins(map, row+1, column,direction);
            #print "South -> ", out_map;
        elif SINK == direction:
            #print "Setting Basin at [%d,%d]" % (row,column);
            next_basin = next_basin + 1;
            out_map[row][column] = basin[next_basin];

        return out_map[row][column];
    else:
        return out_map[row][column];

def printOutputMap():
    i=0;
    while (i<HEIGHT):
        j = 0;
        out_string = "";
        while(j<WIDTH):
            out_string = out_string + " " + out_map[i][j];
            j = j + 1;
        i = i + 1;
        print out_string[1:];


###################################################################################################

f = open("/home/dragon/Desktop/B-large.in");

total_maps = int(f.readline().replace("\n",""));

map = [];
out_map = [];


for t in range(total_maps):
    dim = f.readline().replace("\n","").split();

    HEIGHT = int(dim[0]);
    WIDTH = int(dim[1]);
    least = 99999;
    next_basin = -1;
    
    map = []
    out_map = [];

    for x in range(HEIGHT):
        file_row = f.readline().replace("\n","").split();
        map_row = [];
        out_map_row = [];
        #print file_row;
        for y in range(WIDTH):
            out_map_row.append('-');
            map_row.append(int(file_row[y]));
            
            if (int(file_row[y]) < least):
                least = int(file_row[y]);
        
        map.append(map_row);
        out_map.append(out_map_row);

    #print "Map ==> ", map;
    #print "OutMap ===> ", out_map;
    #print "Least Value is ==> ", least;


    i = 0;
    while (i<HEIGHT):
        j=0;
        while(j<WIDTH):
            if (out_map[i][j] == '-'):
                #print "Calling for [%d, %d] ==> " % (i,j);
                out_map[i][j] = setBasins(map, i, j,getDirection(map,i,j));
            j = j + 1;
        i = i + 1;

    print "Case #%d:" % (t+1);
    printOutputMap();
    #print "";
    
    map = []
    out_map = [];
    #print "---------------------MAP CLOSED------------------------------------";
    #print "";
    #print "";
    #print "";
    #print "";

exit();



    
        


i = 0;
for rows in map:
    j = 0;
    for cell in rows:
        print "%d[%d, %d] ==> " % (cell,i,j) + getDirectionText(getDirection(map,i,j))
        j = j + 1;
    i = i + 1;

#initializeOutputMap();
print "Here is the Initial map";
printOutputMap();




print "Here is the final map";
printOutputMap();





