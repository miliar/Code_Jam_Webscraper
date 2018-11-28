In order to compile the program, you must have the GNU Compiler Collection (GCC) and the Boost libraries properly installed in your machine.
You can download them from:
  http://gcc.gnu.org/ (GCC)
  http://www.boost.org/ (Boost libraries)

Please use GCC version 4.3.0 or newer.

Then, run:
g++ -DBOOST_NO_SLIST -DBOOST_NO_HASH -Wall -std=gnu++0x -o w w.cpp

Once the program is compiled, you can run it with the following command line in GNU/Linux:
./w < B-large.in > B-large.out
