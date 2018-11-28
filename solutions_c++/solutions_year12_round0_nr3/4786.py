CC=g++
CPPFLAGS=-O0 -ggdb
LDFLAGS=-lncurses

DIST=dist

all: recycled_numbers

loader.o: loader.cpp loader.h

counter.o: counter.cpp counter.h

recycled_numbers.o: recycled_numbers.cpp

recycled_numbers: loader.o recycled_numbers.o counter.o
	mkdir -p $(DIST)
	$(CC) $(CPPFLAGS) $(LDFLAGS) -o $(DIST)/recycled_numbers $+

clean:
	rm *.o
	rm -rf dist/
