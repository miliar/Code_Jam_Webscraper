#coding=utf8
# competition 05.03.15 12:09 by mnach #
from . import InputValidation
from io import StringIO


class CaseInput:
    """
    This class represents input of one case in CodeJam
    """
    lines_count = 10

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)
        self._current_line = 0
        self._data = StringIO()

    def feed(self, line):
        if not self.is_full():
            self._save_data(line)
            return self.is_full()
        else:
            raise InputValidation("CaseInput is full, please don't feed it any more!")

    def is_full(self):
        return self._current_line >= self.lines_count

    def _save_data(self, line):
        self._current_line += 1
        self._data.write(line)

    @property
    def data(self):
        return self._data.getvalue()

    def __str__(self):
        if self.is_full():
            return str(self.data)
        else:
            return "Not completed item {!r}".format(self)


class ArrayCaseInput(CaseInput):
    data_converter = int
    do_enumerate = False
    pass_row_num = False

    def __init__(self, **kwargs):
        super(ArrayCaseInput, self).__init__(**kwargs)
        self._data = list()

    @property
    def data(self):
        return self._data

    def _save_data(self, line):
        self._current_line += 1
        for i, data in enumerate(line.split()):
            args = [data]
            if self.do_enumerate:
                args.append(i)
            if self.pass_row_num:
                args.append(self._current_line)
            self._data.append(self.data_converter(*args))
