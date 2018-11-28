CC = g++ -O -Wno-deprecated 
CFLAGS = -g -c

		 
ThemePark: ThemePark.o
	$(CC)  -o ThemePark ThemePark.o 
	
ThemePark.o: ThemePark.cc
	$(CC) $(CFLAGS) ThemePark.cc

clean: 
	rm -rf *.o ThemePark