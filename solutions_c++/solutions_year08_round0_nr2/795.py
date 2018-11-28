.PHONY: all clean

APP = train_timetable

all: $(APP)

$(APP): $(APP).o
	g++ -g -o $@ $(APP).o

CXXFLAGS = -g -O0 -Wall -W -Werror
