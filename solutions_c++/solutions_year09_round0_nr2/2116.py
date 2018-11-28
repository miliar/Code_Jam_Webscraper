RESULT = b
OBJ = $(RESULT).o

CPP = g++
FLAGS = -g -O2 -Wall -Weffc++ -std=c++0x -Wc++0x-compat

INCLUDE   = -I/usr/include/ -I/usr/include/boost/
LIBDIR    =
LIBRARIES = 


.PHONY: all clean

all: $(RESULT)
	@echo 'Done.'

clean:
	rm -f $(OBJ) $(RESULT)
			
$(RESULT): $(OBJ) 
	$(CPP) $(FLAGS) $(OBJ) -o $@ $(LIBDIR) $(LIBRARIES)

%.o: %.cpp 
		$(CPP) $(FLAGS) -c $< -o $@ $(INCLUDE)

run: $(RESULT)
	./$(RESULT)

