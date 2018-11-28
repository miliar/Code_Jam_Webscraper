In order to compile the program, you must have the GNU Compiler Collection (GCC) and the Boost libraries properly installed in your machine.
You can download them from:
  http://gcc.gnu.org/ (GCC)
  http://www.boost.org/ (Boost libraries)
Please use GCC version 4.3.0 or newer.
Then, run:
g++ -Wall -std=gnu++0x -lboost_regex -o alien alien.cpp

Once the program is compiled, you can run it with the following command line in GNU/Linux:
./alien < A-small.in > A-small.out
